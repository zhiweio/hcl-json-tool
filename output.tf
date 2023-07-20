triggers = {
  hcl2json = {
    trigger_hcl2json_test_job = {
      name     = "hcl2json_test_job"
      schedule = "cron(0 3 ? * * *)"
      trigger_actions = {
        test = {
          arguments = {
            "--JOB_COUNTRY" = "CN"
            "--JOB_REGION"  = "cn-north-1"
            "--JOB_RUN"     = "123456"
          }
          connectors = ["slack", "dingtalk", "email"]
          job_name   = "hcl2json-glue-job"
        }
      }
      type = "SCHEDULED"
    }
  }
}
