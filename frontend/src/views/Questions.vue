<template>
  <div>
    <div class="row">
      <div class="col-12">
        <h1>Submit Questions</h1>

        <div class="mb-3">
          <label for="exampleFormControlTextarea1" class="form-label">Your Question</label>
          <textarea
            class="form-control"
            id="exampleFormControlTextarea1"
            rows="3"
            placeholder="Your question goes here"
          ></textarea>
        </div>
        <button class="btn btn-primary mb-3">Submit</button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Question</th>
              <th scope="col">Answers</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>What is the meaning of life?</td>
              <td>
                <ul>
                  <li>Answer 1</li>
                  <li>Answer 2</li>
                  <li>Answer 3</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td>What is the meaning of life?</td>
              <td>
                <ul>
                  <li>Answer 1</li>
                  <li>Answer 2</li>
                  <li>Answer 3</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td>What is the meaning of life?</td>
              <td>
                <ul>
                  <li>Answer 1</li>
                  <li>Answer 2</li>
                  <li>Answer 3</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td>What is the meaning of life?</td>
              <td>
                <ul>
                  <li>Answer 1</li>
                  <li>Answer 2</li>
                  <li>Answer 3</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td>What is the meaning of life?</td>
              <td>
                <ul>
                  <li>Answer 1</li>
                  <li>Answer 2</li>
                  <li>Answer 3</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td>What is the meaning of life?</td>
              <td>
                <ul>
                  <li>Answer 1</li>
                  <li>Answer 2</li>
                  <li>Answer 3</li>
                </ul>
              </td>
            </tr>
          </tbody>
        </table>
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
import { useQuestionStore } from '@/stores/questions'
import { storeToRefs } from 'pinia'

const questionStore = useQuestionStore()

const { questions } = storeToRefs(questionStore)

questionStore.addQuestion({
  id: 1,
  text: 'What is the meaning of life?'
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
  */
})
</script>
