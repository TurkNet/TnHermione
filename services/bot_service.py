from botbuilder.core import TurnContext
from botbuilder.schema import Activity, ActivityTypes
from .chat_service import get_chat_response, clear_chat_history, set_user_language, user_languages
from .translation_service import translate_text

class MyBot:
    async def on_turn(self, turn_context: TurnContext):
        if turn_context.activity.type == "message":
            question = turn_context.activity.text
            user_id = turn_context.activity.from_property.id
            user_name = turn_context.activity.from_property.name if turn_context.activity.from_property.name else "Unknown User"
            
            if user_id not in user_languages:
                user_languages[user_id] = 'tr'

            if question.strip().lower() == "/clean":
                clear_chat_history(user_id)
                response_message = "Sohbet geçmişi temizlendi. Yeni bir konuşma başlatabilirsiniz."
                if user_languages[user_id] != 'tr':
                    response_message = translate_text(response_message, user_languages[user_id])
                await turn_context.send_activity(response_message)
                return

            if question.startswith("/language"):
                _, language = question.split()
                set_user_language(user_id, language)
                response_message = f"Dil {language} olarak ayarlandı"
                if language != 'tr':
                    response_message = translate_text(response_message, language)
                await turn_context.send_activity(response_message)
                return

            await turn_context.send_activity(Activity(type=ActivityTypes.typing))

            response_content = get_chat_response(user_id, user_name, question)
            
            print(f"Kullanıcı: {user_name} ({user_id}) sordu: {question}")
            print(f"Cevap: {response_content}")

            await turn_context.send_activity(response_content)

        elif turn_context.activity.type == "conversationUpdate":
            for member in turn_context.activity.members_added:
                if member.id != turn_context.activity.recipient.id:
                    welcome_message = "Merhaba, ben bir yapay zeka botuyum. Size nasıl yardımcı olabilirim?"
                    if user_languages[member.id] != 'tr':
                        welcome_message = translate_text(welcome_message, user_languages[member.id])
                    await turn_context.send_activity(welcome_message)
