pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
		echo "${TASK_ID}"
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
		bat (script: "python python_functions.py ${TASK_ID})
      }
    }
  }
}

