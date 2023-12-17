<script setup>
  import FilterByState from '@/components/FilterByState.vue'
  import FilterByNumber from '@/components/FilterByNumber.vue'
</script>

<template>
  <div class="container-fluid content overflow-auto">
    <div class="row my-4">
      <div class="col col-2">
        <h4>Incidents List</h4>
      </div>
      <div class="col col-3">
        <FilterByState/>
      </div>
      <div class="col col-3">
        <FilterByNumber/>
      </div>
    </div>
    <div> 
      <table class="table table-striped">
        <thead>
          <tr>
            <th v-for="(column, i) in columns" :key="i" @click="sort(column.field)">
            {{ column.label }}
            <span v-if="sortBy === column.field" :class="sortDesc ? 'arrow-up' : 'arrow-down'"></span>
          </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(data, i) in sortedIncidents" :key="i">
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
              field: '#',
              sortable: false
          },
          {
              label: 'Number',
              field: 'number',
              sortable: true
          },
          {
              label: 'Date',
              field: 'date',
              sortable: true
          },
          {
              label: 'Short description',
              field: 'short_description',
              sortable: false
          },
          {
              label: 'Description',
              field: 'description',
              sortable: false
          },
          {
              label: 'State',
              field: 'state',
              sortable: true
          }              
        ],
        states: {
          1: 'New',
          2: 'In Progress',
          3: 'On Hold',
          6: 'Resolved',
          7: 'Closed',
          8: 'Canceled'
        },
        sortBy: 'date', // Current sorting column
        sortDesc: true // Sort in descending order
      };
    },
    computed: {
      incidents() {
        return this.$store.state.incidents.incidents;
      },
      sortedIncidents() {
        if (this.sortBy) {
          const sortFactor = this.sortDesc ? -1 : 1;
          return this.incidents.slice().sort((a, b) => {
            return a[this.sortBy] > b[this.sortBy] ? sortFactor : -sortFactor;
          });
        } else {
          return this.incidents;
        }
      }
    },
    methods: {
      getIncidents(type) {
        this.$store.dispatch('incidents/getIncidents', type);
      },
      getStateLabel(stateId) {
        return this.states[stateId] || 'Unknown';
      },
      sort(field) {
        const column = this.columns.find(c => c.field === field);
        if (column && column.sortable) {
          if (field === this.sortBy) {
            this.sortDesc = !this.sortDesc;
          } else {
            this.sortBy = field;
            this.sortDesc = false;
          }
        }
      },
    },
    mounted() {
      this.getIncidents("date");
    }
  };
</script>