<template>
  <div class="settings" style="max-width: 480px; margin: 0 auto; padding: 16px;">
    <h3 style="color: #333;">设置</h3>
    <label style="display: block; margin-bottom: 12px;">
      每月预算
      <input v-model="budget" type="number" style="width: 100px; color: #666;">
    </label>
    <button @click="save">保存</button>
  </div>
</template>

<script>
export default {
  name: "SettingsForm",
  data: () => ({ budget: 0 }),
  methods: {
    save() { localStorage.setItem("budget", String(this.budget)) }
  }
}
</script>
