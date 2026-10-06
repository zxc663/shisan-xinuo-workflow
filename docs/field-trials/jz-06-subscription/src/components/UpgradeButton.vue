<template>
  <button class="upgrade-btn" @click="upgrade">
    升级到更高方案（按比例补差价）
  </button>
</template>

<script setup>
const emit = defineEmits(["upgrade"]);

function upgrade() {
  console.log("upgrade clicked");
  emit("upgrade");
}
</script>
