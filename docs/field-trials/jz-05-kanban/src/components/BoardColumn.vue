<template>
  <section
    class="column"
    @dragover.prevent
    @drop.prevent="onDrop"
  >
    <ColumnHeader :name="column.name" :count="tasks.length" />
    <TaskCard
      v-for="t in tasks"
      :key="t.id"
      :task="t"
      @drag-start="$emit('drag-start', $event)"
      @remove="$emit('remove', $event)"
    />
    <p v-else class="empty">这一列还没有任务——从其他列拖一张卡过来，或点「新建任务」。</p>
  </section>
</template>

<script setup>
import TaskCard from "./TaskCard.vue";
import ColumnHeader from "./ColumnHeader.vue";

const props = defineProps({
  column: { type: Object, required: true },
  tasks: { type: Array, default: () => [] },
});
const emit = defineEmits(["drag-start", "remove", "drop"]);

function onDrop(e) {
  emit("drop", { column: props.column.name, event: e });
}
</script>
