<!-- src/components/TaskManager.vue -->
<template>
  <div class="task-manager">
    <h1>Task Manager</h1>
    <form @submit.prevent="addTask">
      <input v-model="newTask" placeholder="Add a new task" />
      <button type="submit">Add Task</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <input
          type="checkbox"
          :checked="task.completed"
          @change="toggleTask(task)"
        />
        <span :class="{ completed: task.completed }">{{ task.title }}</span>
        <button @click="deleteTask(task)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TaskManager',
  data() {
    return {
      tasks: [],
      newTask: '',
    };
  },
  mounted() {
    this.fetchTasks();
  },
  methods: {
    async fetchTasks() {
      const response = await axios.get('http://localhost:8000/api/tasks/');
      this.tasks = response.data;
    },
    async addTask() {
      if (this.newTask.trim()) {
        const response = await axios.post('http://localhost:8000/api/tasks/', {
          title: this.newTask,
        });
        this.tasks.unshift(response.data);
        this.newTask = '';
      }
    },
    async toggleTask(task) {
      const response = await axios.patch(`http://localhost:8000/api/tasks/${task.id}/`, {
        completed: !task.completed,
      });
      Object.assign(task, response.data);
    },
    async deleteTask(task) {
      await axios.delete(`http://localhost:8000/api/tasks/${task.id}/`);
      this.tasks = this.tasks.filter(t => t.id !== task.id);
    },
  },
};
</script>

<style scoped>
.completed {
  text-decoration: line-through;
}
</style>
