import { createStore } from 'vuex'
import IncidentsModule from './incidents.module.js'

export default createStore({
    modules: {
        incidents: IncidentsModule
    }
})