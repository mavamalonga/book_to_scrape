<title>BookToScrape</title>
<h1>Book to Scrape que ce que c'est ?</h1>
<p>
	Book to scrape est un mini programme de scraping écrit en python, son but est de suivre les prix de livres sur le site https://books.toscrape.com.
</p>

<h1>Comment fonctionne ce programme ?</h1>
<p>
	<ul>
		<li>Le programe consulte le site Book to Scrape, extrait toutes les catégories de livres disponibles, puis extrait les informations
	   produit de tous les livres appartenant à toutes les différentes 
	   catégories.</li>
		<li>Les informations suivantes sont récupérées :
			<ul>
				<li>product_page_url</li>
				<li>universal_product_code</li>
				<li>title</li>
				<li>price_including_tax</li>
				<li>price_excluding_tax</li>
				<li>category</li>
				<li>review_rating</li>
				<li>image_url</li>
			</ul>
		</li>
		<li>Les informations récupérées sont écrites dans un fichier csv distinct pour chaque catégorie de livres.</li>
	</ul>
</p>
<h1>Intallation</h1>
<p>
	<ul>
		<li>Lancez un environnement virtuel</li>
		<li>Lancez pip install -r requirements.txt</li>
		<li>Ouvrez un terminal, déplacez vous dans le répertoire principal du projet, lancez l'interpreteur python et, tapez les commandes suivantes :  <ul>
			<li>import os</li>
			<li>path = os.getcwd()</li>
			<li>print(path)</li>
		</ul>
		Récuperez la valeur de path, déplacez vous dans le fichier app.page_content.py, mettez à jour la variable directory et, enregistrez la modification du fichier.
		<li>
			
	

