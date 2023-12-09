<script setup>
  import FilterState from '@/components/FilterState.vue'
</script>

<template>
  <div class="container-fluid content overflow-auto">
    <div class="row my-4">
      <div class="col col-2">
        <h4>Incident List</h4>
      </div>
      <div class="col col-2">
        <FilterState/>
      </div>
    </div>
    <div> 
      <table class="table table-striped">
        <thead>
          <tr>
            <th v-for="(column, i) in columns" :key="i">
              {{ column.label }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(data, i) in incidents" :key="i">
            <td>{{ i + 1 }}</td>
            <td>{{ data.number }}</td>
            <td>{{ data.date }}</td>
            <td>{{ data.short_description }}</td> 
            <td >{{ data.description }}</td>              
            <td class="text-center">{{ getStateLabel(data.state) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: "App",
    data() {
      return {
        columns: [
          {
              label: '#',
              field: '#'
          },
          {
              label: 'Number',
              field: 'number'
          },
          {
              label: 'Date',
              field: 'date'
          },
          {
              label: 'Short description',
              field: 'short_description'
          },
          {
              label: 'Description',
              field: 'description'
          },
          {
              label: 'State',
              field: 'state'
          }              
        ],
        states: {
          1: 'New',
          2: 'In Progress',
          3: 'On Hold',
          6: 'Resolved',
          7: 'Closed',
          8: 'Canceled'
        }
      };
    },
    computed: {
      incidents() {
        return this.$store.state.incidents.incidents;
      }
    },
    methods: {
      getIncidents(type) {
        this.$store.dispatch('incidents/getIncidents', type);
      },
      getStateLabel(stateId) {
        return this.states[stateId] || 'Unknown';
      }
    },
    mounted() {
      this.getIncidents("date");
    }
  };
</script>