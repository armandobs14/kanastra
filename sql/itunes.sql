-- CTE para recuperar artista, gênero e vendas
with itunes_sales as (
  SELECT art.Name as artist,
    gen.Name as genre,
    (inv.UnitPrice * inv.Quantity) as sales
  FROM Track t
    JOIN InvoiceLine inv on t.TrackId = inv.TrackId
    JOIN Album alb on alb.AlbumId = t.AlbumId
    JOIN Artist art on alb.ArtistId = art.ArtistId
    JOIN Genre gen on t.GenreId = gen.GenreId
),
-- CTE para calcular vendas, e porcentagem de vendas
percent_sales as (
  select DISTINCT artist,
    genre,
    sum(sales) OVER (artist_genre_window) as sales,
    sum(sales) OVER (artist_genre_window) / sum(sales) OVER (genre_window) as sales_percentage_by_genre
  from itunes_sales WINDOW genre_window as (PARTITION BY genre),
    artist_genre_window as (PARTITION BY artist, genre)
  order by genre ASC,
    sales_percentage_by_genre DESC
) -- Cálculo de soma cumulativa
SELECT DISTINCT artist,
  genre,
  round(sales, 2) as sales,
  round(100 * sales_percentage_by_genre, 1) as sales_percentage_by_genre,
  round(
    100 * SUM(sales_percentage_by_genre) OVER(
      PARTITION BY genre
      ORDER BY genre ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ),
    1
  ) AS cumulative_sum_by_genre
FROM percent_sales