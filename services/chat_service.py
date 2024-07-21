import openai
from config.config import CHAT_GPT_API_KEY
import ftfy
from .image_service import generate_image
from .filter_service import contains_sensitive_info
from .translation_service import translate_text
from utils.commands import get_help_message

openai.api_key = CHAT_GPT_API_KEY

chat_histories = {}
user_languages = {}

def get_chat_response(user_id, user_name, question):
    if user_id not in chat_histories:
        chat_histories[user_id] = []

    if user_id not in user_languages:
        user_languages[user_id] = 'tr'

    contains_sensitive, line_number, keyword = contains_sensitive_info(question)
    if contains_sensitive:
        response_content = f'<span style="color:red; font-weight:bold;">Mesajınız hassas bilgi içeriyor ve işlenemiyor. "{line_number}" numaralı satırda "{keyword}" anahtar kelimesi bulundu.</span>'
        if user_languages[user_id] != 'tr':
            response_content = translate_text(response_content, user_languages[user_id])
        chat_histories[user_id].append({"role": "assistant", "content": response_content})
        return response_content

    chat_histories[user_id].append({"role": "user", "content": question})

    if question.startswith("/image"):
        prompt = question.replace("/image", "").strip()
        image_url = generate_image(prompt)
        if image_url:
            response_content = f'<img src="{image_url}" alt="Generated Image">'
        else:
            response_content = "Üzgünüm, resmi oluşturamadım."
        if user_languages[user_id] != 'tr':
            response_content = translate_text(response_content, user_languages[user_id])
        chat_histories[user_id].append({"role": "assistant", "content": response_content})
        return response_content

    if question.strip().lower() == "/help" or question.startswith("/"):
        help_message = get_help_message()
        if user_languages[user_id] != 'tr':
            help_message = translate_text(help_message, user_languages[user_id])
        return ftfy.fix_text(help_message)

    messages = [{"role": "system", "content": "Sen herhangi bir konuda soruları cevaplayabilen bir yapay zekasın. Kullanıcı sorgularına detaylı ve bilgilendirici yanıtlar ver."}] + chat_histories[user_id]
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    response_content = gpt_response['choices'][0]['message']['content']

    if user_languages[user_id] != 'tr':
        response_content = translate_text(response_content, user_languages[user_id])

    chat_histories[user_id].append({"role": "assistant", "content": response_content})
    
    print(f"Kullanıcı: {user_name} ({user_id}) sordu: {question}")
    print(f"Cevap: {response_content}")

    return ftfy.fix_text(response_content)

def clear_chat_history(user_id):
    chat_histories[user_id] = []

def set_user_language(user_id, language):
    user_languages[user_id] = language
