param location string
param environmentName string
param workspaceResourceId string

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'edm-obs-ai-${environmentName}-${uniqueString(resourceGroup().id)}'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: workspaceResourceId
  }
}

output applicationInsightsName string = appInsights.name
output connectionString string = appInsights.properties.ConnectionString
