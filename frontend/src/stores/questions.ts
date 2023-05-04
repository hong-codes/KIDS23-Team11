import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export type Question = {
  id: number
  text: string
  status: 'pending' | 'answered' | 'error'
  //answer: string
}

/**
 * This is our global question store. It represents each question asked in the app.
 *
 * Each question here will be sent to the backend API for processing to collect answers by our AI models.
 *
 */
export const useQuestionStore = defineStore('questions', () => {
  const questions = ref<Question[]>([])
  const count = computed(() => questions.value.length)

  function addQuestion(question: Question) {
    // do some api call to add a question
    questions.value.push(question)
  }

  return { count, questions, addQuestion }
})
