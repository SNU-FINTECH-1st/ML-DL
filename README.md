# ML-DL
**이 모델 사투리 마이 묵었다 아이가**
> WORK FLOW : 사투리 TTS -> Translate -> STT 표준어
---

* 모델 돌리기전 필수사항!
  * 꼭 google cloud sdk를 먼저 설치해야함.
  * google cloud token은 유료임을 주의!
  * 무료로 하고 싶으면 다른 tts 사용하시면 됩니다.
    

* fine-tuning된 KoBART 모델 (Huggingface)

  * https://huggingface.co/easyeasy/kobart-snu-bigfin-9th

## 사용된 데이터
- 중·노년층 한국어 방언 데이터(경상도)  
  데이터 출처: [AIHUB 경상도 방언 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71517)

## 필요 패키지
이 프로젝트를 실행하려면 아래의 Python 패키지가 필요합니다.

1. `transformers==4.44.2` - Whisper 및 KoBART 모델 로딩 및 사용.
2. `google-cloud-texttospeech==2.17.2` - Google의 Text-to-Speech API 사용.
3. `gradio==4.42.0` - 사용자 인터페이스 생성.
4. `torch==2.4.0` - PyTorch는 모델 추론을 위해 필요.

## 설치 방법
1. `requirements.txt` 파일을 이용하여 필요한 패키지를 설치합니다.

   ```bash
   pip install -r requirements.txt
   ```

2. 프로젝트를 실행합니다.

   ```bash
   python everyrt.py
   ```

---

## 🧑‍💻 프로젝트 멤버
<table>
  <thead>
    <tr>
      <th><img width="220" alt="image" src="https://github.com/user-attachments/assets/bb353ed1-3234-4eeb-9dad-ad98c1a79cbb"></th>
      <th><img width="220" alt="image" src="https://github.com/user-attachments/assets/bb353ed1-3234-4eeb-9dad-ad98c1a79cbb"></th>
      <th><img width="220" alt="image" src="https://github.com/user-attachments/assets/bb353ed1-3234-4eeb-9dad-ad98c1a79cbb"></th>
      <th><img width="220" alt="image" src="https://github.com/user-attachments/assets/bb353ed1-3234-4eeb-9dad-ad98c1a79cbb"></th>
      <th><img width="220" alt="image" src="https://github.com/user-attachments/assets/bb353ed1-3234-4eeb-9dad-ad98c1a79cbb"></th>
      <th><img width="220" alt="image" src="https://github.com/user-attachments/assets/bb353ed1-3234-4eeb-9dad-ad98c1a79cbb"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/Junparking">박준희👑</a></td>
      <td><a href="https://github.com/bum1123">황현범</a></td>
      <td><a href="https://github.com/BWKBH">김병현</a></td>
      <td><a href="https://github.com/hwankhai">이지환</a></td>
      <td><a href="https://github.com/bigjameschung">정한직</a></td>
      <td><a href="https://github.com/chososo">조하영</a></td>
    </tr>
    <tr>
      <td>- 모델 합병 <br> 데이터전처리 <br> KOBART  </td>
      <td>- KOBART <br> FineTuning </td>
      <td>- TTS Model <br> Research </td>
      <td>- 발표 자료 제작 <br>- WHISPER</td>
      <td>- TTS Model <br> Google cloud api </td>
      <td>- 발표 자료 제작 <br>- WHISPER</td>
    </tr>
  </tbody>
</table>

## DEMO VIEW

<img width="1668" alt="DANDI실행_사진" src="https://github.com/user-attachments/assets/4d80fa21-5d59-4690-a845-3c9bb0111f2c">

