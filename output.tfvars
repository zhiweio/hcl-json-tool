triggers = {
  hcl2json = {
    trigger_hcl2json_test_job = {
      name = "hcl2json_test_job"
      type = "SCHEDULED"
      schedule = "cron(0 3 ? * * *)"
      trigger_actions = {
        test = {
          job_name = "hcl2json-glue-job"
          arguments = {
            "--JOB_RUN" = "123456"
            "--JOB_COUNTRY" = "CN"
            "--JOB_REGION" = "cn-north-1"
          }
          connectors = [
            "slack",
            "dingtalk",
            "email"
          ]
        }
      }
    }
  }
}
