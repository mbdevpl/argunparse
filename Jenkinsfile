#!/usr/bin/env groovy

library 'jenkins-mbdev-pl-libs'

pipeline {

  options {
    ansiColor('xterm')
  }

  environment {
    PYTHON_MODULES = 'argunparse test *.py'
  }

  agent any

  stages {
    stage('Matrix') {
      matrix {

        axes {
          axis {
            name 'PYTHON_VERSION'
            values '3.8', '3.9', '3.10'
          }
        }

        agent {
          dockerfile {
            additionalBuildArgs '--build-arg USER_ID=${USER_ID} --build-arg GROUP_ID=${GROUP_ID}' \
              + ' --build-arg AUX_GROUP_IDS="${AUX_GROUP_IDS}" --build-arg TIMEZONE=${TIMEZONE}' \
              + ' --build-arg PYTHON_VERSION=${PYTHON_VERSION}'
            label 'docker'
          }
        }

        stages {

          stage('Lint') {
            when {
              environment name: 'PYTHON_VERSION', value: '3.10'
            }
            steps {
              sh """#!/usr/bin/env bash
                set -Eeux
                python -m pylint ${PYTHON_MODULES} |& tee pylint.log
                echo "\${PIPESTATUS[0]}" | tee pylint_status.log
                python -m mypy ${PYTHON_MODULES} |& tee mypy.log
                echo "\${PIPESTATUS[0]}" | tee mypy_status.log
                python -m flake518 ${PYTHON_MODULES} |& tee flake518.log
                echo "\${PIPESTATUS[0]}" | tee flake518_status.log
                python -m pydocstyle ${PYTHON_MODULES} |& tee pydocstyle.log
                echo "\${PIPESTATUS[0]}" | tee pydocstyle_status.log
              """
            }
          }

          stage('Test') {
            steps {
              sh '''#!/usr/bin/env bash
                set -Eeuxo pipefail
                TEST_PACKAGING=1 python -m coverage run --branch --source . -m unittest -v
              '''
            }
          }

          stage('Coverage') {
            when {
              environment name: 'PYTHON_VERSION', value: '3.10'
            }
            steps {
              sh '''#!/usr/bin/env bash
                set -Eeux
                python -m coverage report --show-missing |& tee coverage.log
                echo "${PIPESTATUS[0]}" | tee coverage_status.log
              '''
              script {
                defaultHandlers.afterPythonBuild()
              }
            }
          }

          stage('Codecov') {
            environment {
              CODECOV_TOKEN = credentials('codecov-token-mbdevpl-argunparse')
            }
            steps {
              sh '''#!/usr/bin/env bash
                set -Eeuxo pipefail
                python -m codecov --token ${CODECOV_TOKEN}
              '''
            }
          }

        }

      }
    }
  }

  post {
    unsuccessful {
      script {
        defaultHandlers.afterBuildFailed()
      }
    }
    regression {
      script {
        defaultHandlers.afterBuildBroken()
      }
    }
    fixed {
      script {
        defaultHandlers.afterBuildFixed()
      }
    }
  }

}