from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://jenkins_host:8080'
    server = Jenkins(jenkins_url, username='nilaxshi', password='1234')
    return server
    
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print(job_instance.name)
        print(job_instance.get_description())
        print(job_instance.is_running())
        print(job_instance.is_enabled()) 

get_job_details()