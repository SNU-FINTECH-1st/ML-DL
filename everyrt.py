from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from google.cloud import texttospeech
import gradio as gr

# 1. Whisper 모델 로드 (Speech-to-Text)
speech_to_text_pipe = pipeline(model="openai/whisper-large-v3")

# 2. KoBART 모델 로드 (Hugging Face)
model = AutoModelForSeq2SeqLM.from_pretrained('easyeasy/kobart-snu-bigfin-9th')
tokenizer = AutoTokenizer.from_pretrained('easyeasy/kobart-snu-bigfin-9th')

# 3. Google Cloud Text-to-Speech 클라이언트 초기화 (Text-to-Speech)
text_to_speech_client = texttospeech.TextToSpeechClient()

# 음성 인식 함수 (Speech-to-Text)
def transcribe(audio):
    text = speech_to_text_pipe(audio)["text"]
    return text

# 텍스트 변환 함수 (Text-to-Text)
def transform_text(input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=200, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    standard_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return standard_text

# 텍스트를 음성으로 변환하는 함수 (Text-to-Speech)
def synthesize_speech(text):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        name="ko-KR-Standard-D",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = text_to_speech_client.synthesize_speech(
        input=input_text, 
        voice=voice, 
        audio_config=audio_config
    )
    
    # 오디오 파일 생성
    output_filename = "output.mp3"
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
    
    return output_filename

# Gradio 인터페이스 함수 (통합)
def full_pipeline(audio):
    # 1. Speech to Text
    transcribed_text = transcribe(audio)
    
    # 2. Text to Text
    transformed_text = transform_text(transcribed_text)
    
    # 3. Text to Speech
    output_audio = synthesize_speech(transformed_text)
    
    return transcribed_text, transformed_text, output_audio

# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=full_pipeline,
    inputs=gr.Audio(type="filepath", label="입력 오디오 파일"),  # 오디오 파일 입력
    outputs=[
        gr.Textbox(label="음성 인식 결과 (Speech-to-Text)", placeholder="여기에 음성 인식 결과가 표시됩니다..."),
        gr.Textbox(label="텍스트 변환 결과 (Text-to-Text)", placeholder="여기에 텍스트 변환 결과가 표시됩니다..."),
        gr.Audio(label="최종 음성 출력 (Text-to-Speech)")
    ],
    title="음성 처리 파이프라인",
    description=(
        "이 애플리케이션은 오디오 파일을 업로드하거나 음성을 녹음할 수 있습니다. "
        "음성을 텍스트로 변환하고, 변환된 텍스트를 언어 모델을 사용하여 수정하며, "
        "수정된 텍스트를 다시 음성으로 변환합니다."
    ),
    article=(
        "<div style='text-align: center; margin-top: 20px;'>"
        "<h2>이 애플리케이션을 사용하는 방법:</h2>"
        "<ol>"
        "<li>'마이크로부터 녹음'을 클릭하거나 오디오 파일을 업로드하세요.</li>"
        "<li>애플리케이션이 음성을 텍스트로 변환할 때까지 기다리세요.</li>"
        "<li>변환된 텍스트를 확인하고, 생성된 음성을 들어보세요.</li>"
        "</ol>"
        "</div>"
    ),
    theme="monochrome"  # 여기서 원하는 테마로 변경 가능
)

# Gradio 인터페이스 실행
iface.launch()