import { z } from "zod";

export const CalificacionSchema = z.object({
  calificacion: z.number(),
  id: z.number(),
  receta_id: z.number(),
});

export const ComentarioSchema = z.object({
  contenido: z.string(),
  id: z.number(),
  receta_id: z.number(),
});

export const ImagenSchema = z.object({
  download_url: z.string(),
  file_name: z.string(),
  file_type: z.string(),
  id: z.number(),
  receta_id: z.number(),
});

export const RecetaSchema = z.object({
  calificaciones: z.array(CalificacionSchema),
  comentarios: z.array(ComentarioSchema),
  descripcion: z.string(),
  fecha_creacion: z.string(), // Puedes usar z.coerce.date() si quieres convertirlo automáticamente
  id: z.number(),
  imagenes: z.array(ImagenSchema),
  ingredientes: z.string(),
  preparacion: z.string(),
  promedio_calificacion: z.number().nullable(),
  titulo: z.string(),
});

// Schema para obtener una sola receta
export const RecetaResponseSchema = z.object({
  data: RecetaSchema
})

export const RecetasResponseSchema = z.object({
  data: z.array(RecetaSchema),
});

export const formRecetaSchema = z.object({
  titulo: z.string(),
  descripcion: z.string(),
  ingredientes: z.string(),
  preparacion: z.string()
})

export type FormReceta = z.infer<typeof formRecetaSchema>

// Tipos TypeScript
export type RecetasResponse = z.infer<typeof RecetasResponseSchema>;
export type Receta = z.infer<typeof RecetaSchema>

// comment
export const commentSchema = z.object({
  contenido: z.string()
})
export type Comment = z.infer<typeof commentSchema>