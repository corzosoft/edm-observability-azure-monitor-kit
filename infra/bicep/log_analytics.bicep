param location string
param environmentName string

resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: 'edm-obs-law-${environmentName}-${uniqueString(resourceGroup().id)}'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

output workspaceId string = workspace.id
output workspaceName string = workspace.name
