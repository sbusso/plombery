import path from 'path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  plugins: [react()],
  build: {
    sourcemap: true,
    // rollupOptions: {
    //   output: {
    //     manualChunks: (id) => {
    //       if (id.includes('node_modules')) {
    //         if (id.includes('handsontable')) return 'table'
    //         if (id.includes('react')) return 'vendor'
    //         if (id.includes('@tremor') || id.includes('@headlessui')) return 'ui'
    //         if (id.includes('@tanstack') || id.includes('socket.io')) return 'data'
    //         return 'deps'
    //       }
    //     },
    //   },
    // },
    chunkSizeWarningLimit: 500,
  },
})
