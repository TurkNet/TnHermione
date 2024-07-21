# TnHermione

[English](#english) | [Türkçe](#türkçe)

---

## English

### TnHermione

TnHermione is an AI-powered chatbot designed to assist users with a variety of tasks. This bot can answer questions, generate images based on prompts, and switch between different languages to provide a personalized experience.

### Features

- **Answering Questions**: Provides detailed and informative responses to user queries.
- **Image Generation**: Generates images based on user prompts.
- **Language Support**: Supports multiple languages and can switch languages based on user preference.
- **Sensitive Information Filtering**: Detects and filters out sensitive information in user messages.
- **Command Support**: Recognizes and executes a set of predefined commands.
- **Prometheus Metrics**: Provides a `/metrics` endpoint for Prometheus to scrape.

### Commands

- **/clean**: Clears the chat history. Usage: `/clean`
- **/language**: Changes the user's language preference. Usage: `/language <language_code>` (e.g., `/language en`)
- **/image**: Generates an image based on the provided prompt. Usage: `/image <prompt>` (e.g., `/image a sunset over a mountain`)
- **/help**: Displays the list of supported commands and their usage. Usage: `/help`

### API Endpoints

- **GET /**: Used to verify that the application is running.
- **POST /api/ask**: Used to answer user questions.
  - Request Body:
    ```json
    {
      "question": "your question here",
      "user_id": "user_id"
    }
    ```
  - Response:
    ```json
    {
      "answer": "Response from the AI"
    }
    ```
- **POST /api/messages**: Used for integration with Microsoft Teams.
- **GET /metrics**: Provides Prometheus metrics for monitoring.

### Installation

1. Clone the repository

2. Navigate to the project directory:
    ```bash
    cd tnhermione
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables:
    ```bash
    cp .env.example .env
    # Edit the .env file and add your API keys and other settings
    ```

6. Run the application:
    ```bash
    python app.py
    ```

### Using Docker

You can also run the application using Docker.

1. Build the Docker image:
    ```bash
    docker build -t tnhermione .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 3978:3978 --env-file .env tnhermione
    ```

---

## Türkçe

### TnHermione

TnHermione, kullanıcılara çeşitli görevlerde yardımcı olmak için tasarlanmış yapay zeka destekli bir sohbet botudur. Bu bot, soruları cevaplayabilir, istemlere dayalı olarak görüntüler oluşturabilir ve kullanıcı tercihine göre farklı diller arasında geçiş yapabilir.

### Özellikler

- **Soruları Cevaplama**: Kullanıcı sorgularına ayrıntılı ve bilgilendirici yanıtlar sağlar.
- **Görüntü Oluşturma**: Kullanıcı istemlerine dayalı olarak görüntüler oluşturur.
- **Dil Desteği**: Birden fazla dili destekler ve kullanıcı tercihine göre dil değiştirebilir.
- **Hassas Bilgi Filtreleme**: Kullanıcı mesajlarındaki hassas bilgileri tespit eder ve filtreler.
- **Komut Desteği**: Önceden tanımlanmış bir dizi komutu tanır ve uygular.
- **Prometheus Metrikleri**: Prometheus'un toplaması için `/metrics` endpointi sağlar.

### Komutlar

- **/clean**: Sohbet geçmişini temizler. Kullanım: `/clean`
- **/language**: Kullanıcının dil tercihlerini değiştirir. Kullanım: `/language <dil_kodu>` (örneğin, `/language en`)
- **/image**: Belirtilen isteme dayalı olarak bir resim oluşturur. Kullanım: `/image <istem>` (örneğin, `/image a sunset over a mountain`)
- **/help**: Desteklenen komutları ve kullanım örneklerini gösterir. Kullanım: `/help`

### API Endpoints

- **GET /**: Uygulamanın çalıştığını doğrulamak için kullanılır.
- **POST /api/ask**: Kullanıcının sorularını yanıtlamak için kullanılır.
  - Request Body:
    ```json
    {
      "question": "sorunuz burada",
      "user_id": "kullanıcı_id"
    }
    ```
  - Response:
    ```json
    {
      "answer": "Yapay zeka tarafından verilen yanıt"
    }
    ```
- **POST /api/messages**: Microsoft Teams ile entegrasyon için kullanılır.
- **GET /metrics**: İzleme için Prometheus metriklerini sağlar.

### Kurulum

1. Repoyu klonlayın

2. Proje dizinine gidin:
    ```bash
    cd tnhermione
    ```

3. Bir sanal ortam oluşturun ve etkinleştirin:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Windows'da `venv\Scripts\activate` kullanın
    ```

4. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

5. Çevre değişkenlerini ayarlayın:
    ```bash
    cp .env.example .env
    # .env dosyasını düzenleyin ve API anahtarlarınızı ve diğer ayarları ekleyin
    ```

6. Uygulamayı çalıştırın:
    ```bash
    python app.py
    ```

### Docker Kullanımı

Uygulamayı Docker kullanarak da çalıştırabilirsiniz.

1. Docker imajını oluşturun:
    ```bash
    docker build -t tnhermione .
    ```

2. Docker konteynerini çalıştırın:
    ```bash
    docker run -d -p 3978:3978 --env-file .env tnhermione
    ```

---
