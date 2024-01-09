import { createStore } from 'vuex'
import GetIncidentsModule from './get_incidents.module.js'
import CreateIncidentModule from './create_incident.module.js'
import DeleteIncidentModule from './delete_incident.module.js'
import UpdateIncidentModule from './update_incident.module.js'

export default createStore({
    modules: {
        get_incidents: GetIncidentsModule,
        create_incident: CreateIncidentModule,
        delete_incident: DeleteIncidentModule,
        update_incident: UpdateIncidentModule
    }
})