<template>
  <div >
    <h1>About</h1>

    <!-- add paragraph tags below -->
    <p>This project is the frontend for the bio hackathon TEAM 11 - at st.jude. Read more about the project at the project Wiki.</p>
    <p>The frontend provides the following capabilities:</p>
<p>
  <ul>
    <li>Lets users submit a question for the ML engine to retreive the answers from 4 pre-determined model types.
      <ul>

      <li>The frontend will submit this to the ML model and wait - via polling :(</li>

      <li>Frontend will allow users to submit more than one question, so that the user does not have to wait for API to finish</li>

      <li>Frontend is also responsible for POSTing the results to another django backend that will store the questions+answers in a database</li>
      </ul>

    </li>

<li>In a separate area, the users can enter "Ranking" UI. The ranking UI will only show questions that have been fully processed by the ML (i.e. all answers are ready)
  <ul>
      <li>In the ranking UI, users will submit a rating for each answer</li>
      <li>The ranking UI should indicate which questions are rated and which ones are pending a rating.</li>
  </ul>
</li>
  </ul>
</p>
  </div>
</template>