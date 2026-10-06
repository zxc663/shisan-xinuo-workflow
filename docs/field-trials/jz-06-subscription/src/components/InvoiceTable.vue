<template>
  <section class="invoice-table">
    <h2>历史账单</h2>
    <table>
      <thead>
        <tr><th>月份</th><th>金额</th><th>状态</th><th>操作</th></tr>
      </thead>
      <tbody>
        <tr v-for="inv in invoices" :key="inv.id">
          <td>{{ inv.month }}</td>
          <td>{{ inv.amount }}</td>
          <td>{{ inv.paid ? "已支付" : "待支付" }}</td>
          <td><button @click="download(inv)">下载发票</button></td>
        </tr>
        <tr v-else>
          <td colspan="4">还没有账单——开通订阅后这里会按月出账。</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
defineProps({ invoices: { type: Array, default: () => [] } });
const emit = defineEmits(["download"]);

function download(inv) {
  emit("download", inv);
}
</script>
