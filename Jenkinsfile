pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
		echo "${TASK_ID}"
		echo "${APPLICATION_NAME}"
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
		bat 'python python_functions.py ${TASK_ID},${APPLICATION_NAME}'
      }
    }
  }
}

