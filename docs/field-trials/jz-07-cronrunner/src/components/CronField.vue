<template>
  <input v-model="expr" placeholder="* * * * *" />
</template>

<script setup>
import { ref } from 'vue'

const expr = ref('')

// registry: source=brief 原子需求 1「能新建定时任务（名称+cron 表达式）」
</script>
