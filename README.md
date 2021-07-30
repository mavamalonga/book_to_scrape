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
<h1>Intallation et éxecution du programme</h1>
<p>
	<ul>
		Assurez vous d'avoir installez le gestionnaire de version git en local.
		Ensuite ouvrez le terminal git et, suivez les étapes ci-dessous.
		1.Initialise le répertoire courant.
		<li>git init</li>
		2.Clonez le respository github en local
		<li>git clone https://github.com/mavamalonga/book_to_scrape.git</li>
		3.Placez vous dans le répertoire principal du projet et, créez un invironnement virtuel
		<li>python -m venv env</li>
		4.Lancez l'environnement virtuel
		<li>env\Scripts\activate.bat</li>
		5.Installez les paquets python avec le gestionaire de paquets pip
		<li>pip install -r requirements.txt</li>
		6.Lancez le programme avec le fichier run
		<li>python run.py</li>
</p>

	

