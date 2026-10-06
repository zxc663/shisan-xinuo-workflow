<template>
  <section class="key-table">
    <h2>我的密钥</h2>
    <table>
      <thead>
        <tr><th>名称</th><th>指纹</th><th>状态</th><th>操作</th></tr>
      </thead>
      <tbody>
        <tr v-for="k in keys" :key="k.id">
          <td>{{ k.name }}</td>
          <td>{{ k.fingerprint }}</td>
          <td>{{ k.status === "active" ? "启用" : "已吊销" }}</td>
          <td>
            <button v-if="k.status === 'active'" @click="revoke(k)">吊销</button>
            <button @click="viewUsage(k)">用量</button>
          </td>
        </tr>
        <tr v-else>
          <td colspan="4">还没有密钥——点右上角「生成密钥」创建第一把。</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
import { ref } from "vue";

const keys = ref([]);
const emit = defineEmits(["revoke", "view-usage"]);

function revoke(k) {
  emit("revoke", k);
}

function viewUsage(k) {
  emit("view-usage", k);
}
</script>
