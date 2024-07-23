SUPPORTED_COMMANDS = {
    "/clean": "Sohbet geçmişini temizler. Kullanım: /clean",
    "/language": "Kullanıcının dil tercihlerini değiştirir. Kullanım: /language <dil_kodu> (örneğin, /language en)",
    "/image": "Belirttiğiniz prompt'a göre bir resim oluşturur. Kullanım: /image <resim_isteği> (örneğin, /image a sunset over a mountain)",
    "/help": "Desteklenen komutları ve kullanım örneklerini gösterir. Kullanım: /help",
    "/nolog": "Mesaj ve yanıtların loglanmasını kapatır. Kullanım: /nolog",
    "/log": "Mesaj ve yanıtların loglanmasını açar. Kullanım: /log"
}

def get_help_message():
    help_message = "Desteklenen komutlar:\n\n"
    for command, description in SUPPORTED_COMMANDS.items():
        help_message += f"**{command}**\n{description}\n\n"
    return help_message
