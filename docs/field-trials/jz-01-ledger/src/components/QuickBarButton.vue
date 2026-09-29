<template>
  <div class="quick-add"
       style="position: fixed; right: 24px; bottom: 24px; background: #1890ff; color: white;
              border-radius: 50%; width: 56px; height: 56px; text-align: center;
              line-height: 56px; font-size: 28px; cursor: pointer;"
       @click="$emit('open')">＋</div>
</template>

<script>
export default { name: "QuickBarButton", emits: ["open"] }
</script>
