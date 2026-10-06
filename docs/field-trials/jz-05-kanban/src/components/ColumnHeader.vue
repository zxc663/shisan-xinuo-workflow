<template>
  <header class="column-header">
    <h3>{{ name }}</h3>
    <span class="count">{{ count }}</span>
  </header>
</template>

<script setup>
defineProps({
  name: { type: String, required: true },
  count: { type: Number, default: 0 },
});
</script>
