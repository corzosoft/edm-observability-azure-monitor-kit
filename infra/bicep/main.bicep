targetScope = 'resourceGroup'

param location string = resourceGroup().location
param environmentName string = 'dev'
param alertEmail string

module law 'log_analytics.bicep' = {
  name: 'logAnalytics'
  params: {
    location: location
    environmentName: environmentName
  }
}

module appi 'application_insights.bicep' = {
  name: 'applicationInsights'
  params: {
    location: location
    environmentName: environmentName
    workspaceResourceId: law.outputs.workspaceId
  }
}

module actions 'action_groups.bicep' = {
  name: 'actionGroups'
  params: {
    location: location
    environmentName: environmentName
    alertEmail: alertEmail
  }
}

module alerts 'alert_rules.bicep' = {
  name: 'alertRules'
  params: {
    location: location
    environmentName: environmentName
    workspaceResourceId: law.outputs.workspaceId
    actionGroupId: actions.outputs.actionGroupId
  }
}

output workspaceName string = law.outputs.workspaceName
output applicationInsightsName string = appi.outputs.applicationInsightsName
