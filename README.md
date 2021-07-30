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
	Assurez vous d'avoir installé en local le gestionnaire de version git et le gestionnaire de paquets python pip.<br>
	Ouvrez le terminal git et, suivez les étapes ci-dessous.
	<ol>
		<li>Initialise le répertoire courant
			<ul>
				<li>git init</li>
			</ul>
		</li>
		<li>Clonez le respository github en local<br>
			<ul>
				<li>git clone https://github.com/mavamalonga/book_to_scrape.git</li>
			</ul>
		</li>
		<li>Placez vous dans le répertoire principal du projet et, créez un environnement virtuel<br>
			<ul>
				<li>python -m venv env</li>
			</ul>
		</li>
		<li>Lancez l'environnement virtuel
			<ul>
				<li>env\Scripts\activate.bat</li>
			</ul>
		</li>
		<li>Installez les paquets python avec le gestionnaire de paquets pip
			<ul>
				<li>pip install -r requirements.txt</li>
			</ul>
		</li>
		<li>Lancez le programme avec le fichier run.py
			<ul>
				<li>python run.py</li>
			</ul>
		</li>
	</ol>
	<br>
	Les fichiers générés par le programme seront sauvegardés dans le dossier csv du resperoire principal.<br>
	Pour toute autre question, contactez moi à l'adresse suivante : mavamalonga.alpha@gmail.com
</p>

	

