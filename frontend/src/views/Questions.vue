<template>
  <div>
    <div class="row">
      <div class="col-12">
        <h1>Submit Questions</h1>

        <div class="mb-3">
          <label for="exampleFormControlTextarea1" class="form-label">Your Question</label>
          <textarea
            v-model="questionText"
            class="form-control"
            id="exampleFormControlTextarea1"
            rows="4"
            placeholder="Your question goes here"
          ></textarea>
          <div id="passwordHelpBlock" class="form-text">
            The question you submit here will be sent to our AI models for answering. The models
            might take a while to respond - but you do not need to wait for them to finish. You can
            continue adding questions and the questions will be processed in the background. PLEASE
            DO NOT CLOSE THIS TAB!
          </div>
        </div>

        <button class="btn btn-primary mb-3" @click="addQuestion">Submit</button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Question</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="q in questions" :key="q.id">
              <td>{{ q.id }}</td>
              <td>{{ q.text }}</td>
              <td>
                <i v-if="q.status == 'pending'" class="fas fa-spin fa-spinner text-warning"></i>
                <i v-if="q.status == 'answered'" class="fas fa-check-circle text-success"></i>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!--
      <div class="col-4">
        <QuestionList :questions="questions" />
      </div>
      <div class="col-8">
        <QuestionDetail :question="questions[0]" />
      </div>
      -->
    </div>
  </div>
</template>

<script setup lang="ts">
import QuestionList from './questions/QuestionList.vue'
import QuestionDetail from './questions/QuestionDetail.vue'
import { useQuestionStore } from '@/stores/questions'
import { storeToRefs } from 'pinia'
import { ref } from 'vue'

const questionText = ref('')

const questionStore = useQuestionStore()
const { questions, count } = storeToRefs(questionStore)

const addQuestion = () => {
  questionStore.addQuestion({
    id: count.value + 1,
    text: questionText.value,
    status: 'pending'
  })
}

/*
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
})
  */
</script>
