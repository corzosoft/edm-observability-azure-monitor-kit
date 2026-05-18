param location string
param environmentName string
param workspaceResourceId string
param actionGroupId string

resource failedJobs 'Microsoft.Insights/scheduledQueryRules@2023-03-15-preview' = {
  name: 'edm-failed-jobs-${environmentName}'
  location: location
  properties: {
    displayName: 'EDM failed jobs'
    enabled: true
    scopes: [workspaceResourceId]
    severity: 2
    evaluationFrequency: 'PT5M'
    windowSize: 'PT15M'
    criteria: {
      allOf: [
        {
          query: 'AppTraces | extend p=parse_json(Message) | where tostring(p.event_name) == "job_completed" and tostring(p.job_status) == "FAILED"'
          timeAggregation: 'Count'
          operator: 'GreaterThan'
          threshold: 0
        }
      ]
    }
    actions: {
      actionGroups: [actionGroupId]
    }
  }
}

resource slaBreach 'Microsoft.Insights/scheduledQueryRules@2023-03-15-preview' = {
  name: 'edm-sla-breach-${environmentName}'
  location: location
  properties: {
    displayName: 'EDM SLA breach'
    enabled: true
    scopes: [workspaceResourceId]
    severity: 2
    evaluationFrequency: 'PT15M'
    windowSize: 'PT30M'
    criteria: {
      allOf: [
        {
          query: 'AppTraces | extend p=parse_json(Message) | where todouble(p.duration_ms) > 1800000'
          timeAggregation: 'Count'
          operator: 'GreaterThan'
          threshold: 0
        }
      ]
    }
    actions: {
      actionGroups: [actionGroupId]
    }
  }
}
