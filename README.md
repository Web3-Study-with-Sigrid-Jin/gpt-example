# SOPT GPT 스터디 3주차 및 4주차

## 주제

* GPT를 활용한 Finetuning과 Few-shot Training, 어떻게 할 것인가?
  * 내부 LLM에 접근할 수 없다면, 즉 외부 API 인터페이스로만 통신한다면?
  * In-Context Learning와 Indexing이 유용한 방법이다.
  * Fine-tuning은 Few-shot Training을 활용할 때 토큰 수를 줄이고 반복 프롬프트 작업을 줄이기 위한 방법이다.
  * Indexing은 많은 분량의 파일이나 데이터를 학습시키기 위한 유용한 방법이다.
* 스터디 일정: '23. 5. 2 (화) 22:00 ~ 24:00

## 3주차 실습 내용

1. [Fine-tuning & In-Context Learning] Scale AI의 Scrollbook을 활용하여 Few-shot training을 실습해보고, Fine-tuning 모델 생성과의 차이점을 이해한다.
   * https://spellbook.scale.com/
   * https://platform.openai.com/docs/guides/fine-tuning
2. [Indexing] LlamaIndex를 연습해보고 HTML/PDF 등의 파일을 LLM에게 학습시켜본다.
   * https://colab.research.google.com/drive/1BS_HloCRCSDZU06dKCcNXuFVDQJ8yUEr#scrollTo=vigz-lUhx9YJ
3. [Integration] ChatGPT를 활용한 간단한 추천시스템을 만들어본다.
   * https://colab.research.google.com/drive/1BA7YewVUvO9eappNHrW0bYAKYKx_GcgS?usp=sharing

## 4주차 실습 내용

* BabyAGI, SerpAPI 그리고 Streamlit을 활용하여 Todo List 작성과 리서치 수행을 대신해주는 간단한 Agent-GPT를 만들어본다.
  * 저장소 내의 `your-gpt-agent` 디렉토리 완성본을 참고해본다.
  * https://colab.research.google.com/drive/11w-XCj3f4bT8w2SIMuY9BpZsYwftXLOp#scrollTo=6e0305eb

* Pinecone을 사용하여 장기 기억 애플리케이션을 만들어본다.
  * https://colab.research.google.com/drive/13wben2cKOAJEEDAUpG3uaEnVifp89FoH#scrollTo=t6eJQg1yVDMT

## 읽을 거리

* https://magazine.sebastianraschka.com/p/finetuning-large-language-models
* https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb
