import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Frontend calls /api/* (backend, :8000) and /ai/* (AI service, :8001)
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": { target: "http://localhost:8000", ws: true, changeOrigin: true },
      "/ai": { target: "http://localhost:8001", changeOrigin: true },
    },
  },
});
