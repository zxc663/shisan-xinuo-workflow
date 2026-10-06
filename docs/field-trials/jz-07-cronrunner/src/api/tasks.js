// mock 后端声明（backs.txt 对应实现面）
// 端点：GET /tasks、POST /tasks、DELETE /tasks/{id}、
//       GET /tasks/{id}/history、POST /tasks/{id}/toggle

export async function toggleTask(id) {
  try {
    await fetch(`/api/tasks/${id}/toggle`, { method: 'POST' })
  } catch (e) {}
}

export async function deleteTask(id) {
  try {
    await fetch(`/api/tasks/${id}`, { method: 'DELETE' })
  } catch (e) {
    // 删除失败暂不处理
    throw e
  }
}
