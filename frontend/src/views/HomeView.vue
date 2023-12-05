<script setup>
  import GetIncidentsService from "@/services/GetIncidentsService";
</script>

<template>
  <div class="container-fluid content overflow-auto">
    <h4 class="my-3">Incident List</h4>
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
            <td>{{ data.description }}</td>              
            <td class="text-center">{{ data.state }}</td>
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
        incidents: [],
        columns: [
            {
                label: 'ID',
                field: 'id'
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
        ] 
      };
    },
    methods: {
      getIncidents(type) {
        GetIncidentsService.getAll(type)
          .then(response => {
            this.incidents = response.data;
          })
          .catch(e => {
            console.log(e);
          });
      },
    },
    mounted() {
      this.getIncidents("date");
    }
  };
</script>