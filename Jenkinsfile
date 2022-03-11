def  SendNotification(status, user) {
	echo status
	 sh "python3 $WORKSPACE/chatbot.py \"$JOB_NAME\" \"$user\" \"$BUILD_NUMBER\" \"$BUILD_URL\" $status" 
}

def GetBuildUser(){
    wrap([$class: 'BuildUser']) {
        return "${BUILD_USER}"
    }
}
pipeline {
    agent any
	environment {
            chat = credentials('CHATBOT')
    }
	
	stages {
			/*stage("Checkout"){
			steps{
					git branch: 'main', url: 'https://github.com/Nilakshi23/test2.git'		
					sh 'pip3 install httplib2'
					}
			} */
		
		stage("Sonar Scanning"){
			steps{
			sh '''
			cd /var/lib/jenkins/workspace/SonarAnalysis/ && /opt/sonar-scanner/sonar-scanner-4.6.2.2472-linux/bin/sonar-scanner -X -D sonar.projectKey=sonarqubetest -D sonar.login=$SONAR_TOKEN -D sonar.sources=. -D sonar.host.url=http://3.91.146.109:9000/ -D sonar.projectName=Test -D sonar.projectVersion=1.0 
	         SONAR_QG_URL="${SONAR_URL}/api/qualitygates/project_status?projectKey=${SONAR_PROJECT_KEY}"
			 SONAR_QG_RESULT=$(curl -s -u "${SONAR_TOKEN}:" $SONAR_QG_URL)
			 QG_STATUS=$(echo $SONAR_QG_RESULT | jq -r .projectStatus.status)
			 echo "Fetched Quality Gate status ---->  ${QG_STATUS}"
			 curl -u $SONAR_TOKEN ${SONAR_QG_URL} --output testfile.json
			 SonarQubeQualityGateStatus=$( jq -r ".projectStatus.status" testfile.json)
			 if [ "$SonarQubeQualityGateStatus" != "OK" ]; then
				echo "Quality Gate failed"
			 else
				echo "Quality Gate Successful"
			 fi	
			 
			'''
	
			}
		} 
    }
post {
    success {
        SendNotification("SUCCESSFUL", GetBuildUser());
             }
    unstable {
          SendNotification("UNSTABLE", GetBuildUser());
             }
    failure {
           SendNotification("FAILED", GetBuildUser());
	    }
    }
    
}
