param location string
param environmentName string
param alertEmail string

resource actionGroup 'Microsoft.Insights/actionGroups@2023-01-01' = {
  name: 'edm-obs-ag-${environmentName}'
  location: 'global'
  properties: {
    groupShortName: 'edmobs'
    enabled: true
    emailReceivers: [
      {
        name: 'support-email'
        emailAddress: alertEmail
        useCommonAlertSchema: true
      }
    ]
  }
}

output actionGroupId string = actionGroup.id
