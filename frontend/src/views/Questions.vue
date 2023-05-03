<script setup lang="ts"></script>

<template>
  <div>
    <div class="row">
      <div class="col-12">
        <h1>Questions</h1>
      </div>
      <div class="col-4">
        <QuestionList :questions="questions" />
      </div>
      <div class="col-8">
        <QuestionDetail :question="questions[0]" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import QuestionList from './questions/QuestionList.vue'
import QuestionDetail from './questions/QuestionDetail.vue'
import { ref } from 'vue'

let questions = ref([])

questions.value.push([
  {
    text: 'What is the meaning of life?',
    answers: [
      {
        type: 'ChatGPT',
        text: 'Answer 1',
        scores: {
          biomedical: 3,
          general: 3
        }
      },
      {
        type: 'BioGPT',
        text: 'Answer 1',
        scores: {
          biomedical: 3,
          general: 3
        }
      },
      {
        type: 'AI21',
        text: 'Answer 1',
        scores: {
          biomedical: 3,
          general: 3
        }
      },
      {
        type: 'OpenAssistant',
        text: 'Answer 1',
        scores: {
          biomedical: 3,
          general: 3
        }
      }
    ]
  }
])
</script>
