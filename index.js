var ig = require('instagram-scraping');

ig.scrapeTag('hiram.dev').then((result) => {
  console.dir(result);
});
// import express from "express";
// import InstagramScraper from "instagram-scraping";

// const app = express();
// const port = process.env.PORT || 3000;

// app.get("/profile", async (req, res) => {
//   try {
//     // Especifica el nombre de usuario del perfil
//     const username = "hiram.dev";

//     // Crea una instancia de InstagramScraper
//     const scraper = new InstagramScraper();

//     // Obtén los datos del perfil, incluidos los datos de los posts
//     const profile = await scraper.getAccount(username);

//     // Extrae la descripción del perfil y el número de seguidores
//     const descripcion = profile.biography;
//     const seguidores = profile.followedByCount;

//     // Extrae las URL de las imágenes de los posts
//     const posts = profile.posts.map((post) => ({
//       imageURL: post.display_url,
//     }));

//     res.json({ descripcion, seguidores, posts });
//   } catch (error) {
//     // Imprime el error completo para obtener más detalles
//     console.error("Error:", error);
//     res
//       .status(500)
//       .json({ error: "Error al obtener datos del perfil de Instagram" });
//   }
// });

// app.listen(port, () => console.log(`Servidor escuchando en el puerto ${port}`));
