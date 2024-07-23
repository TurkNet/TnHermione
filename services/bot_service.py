from botbuilder.core import TurnContext
from botbuilder.schema import Activity, ActivityTypes, Attachment
from .chat_service import get_chat_response, clear_chat_history, set_user_language, user_languages
from .translation_service import translate_text
from utils.codeblocks import extract_code_blocks, detect_language

log_preferences = {}

class MyBot:
    async def on_turn(self, turn_context: TurnContext):
        if turn_context.activity.type == "message":
            question = turn_context.activity.text
            user_id = turn_context.activity.from_property.id
            user_name = turn_context.activity.from_property.name if turn_context.activity.from_property.name else "Unknown User"
            
            if user_id not in user_languages:
                user_languages[user_id] = 'tr'
            
            if user_id not in log_preferences:
                log_preferences[user_id] = True

            if question.strip().lower() == "/clean":
                clear_chat_history(user_id)
                log_preferences[user_id] = True
                response_message = "Sohbet geçmişi temizlendi. Yeni bir konuşma başlatabilirsiniz."
                if user_languages[user_id] != 'tr':
                    response_message = translate_text(response_message, user_languages[user_id])
                await turn_context.send_activity(response_message)
                return

            if question.strip().lower() == "/nolog":
                log_preferences[user_id] = False
                response_message = "Loglama kapatıldı."
                if user_languages[user_id] != 'tr':
                    response_message = translate_text(response_message, user_languages[user_id])
                await turn_context.send_activity(response_message)
                return

            if question.strip().lower() == "/log":
                log_preferences[user_id] = True
                response_message = "Loglama açıldı."
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
            
            if log_preferences[user_id]:
                print(f"Kullanıcı: {user_name} ({user_id}) sordu: {question}")
                print(f"Cevap: {response_content}")

            combined_content = ""
            parts = response_content.split('```')

            for i, part in enumerate(parts):
                if i % 2 == 0:
                    combined_content += part
                else:
                    codeblock_lines = part.split('\n')
                    if codeblock_lines and codeblock_lines[0].startswith('```') and codeblock_lines[0].endswith('```'):
                        code_language = codeblock_lines[0].strip('```')
                        code_content = '\n'.join(codeblock_lines[1:])
                    else:
                        code_language = detect_language(part)
                        code_content = '\n'.join(codeblock_lines)
                    
                    card_content = {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "CodeBlock",
                                "codeSnippet": f"{code_content}",
                                "wrap": True,
                                "language": code_language
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "version": "1.5"
                    }

                    card_attachment = Attachment(content_type="application/vnd.microsoft.card.adaptive", content=card_content)
                    combined_content += f"\n```{code_content}```\n\n"
            await turn_context.send_activity(combined_content)

        elif turn_context.activity.type == "conversationUpdate":
            for member in turn_context.activity.members_added:
                if member.id != turn_context.activity.recipient.id:
                    welcome_message = "Merhaba, ben bir yapay zeka botuyum. Size nasıl yardımcı olabilirim?"
                    if user_languages[member.id] != 'tr':
                        welcome_message = translate_text(welcome_message, user_languages[member.id])
                    await turn_context.send_activity(welcome_message)
