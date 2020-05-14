GENERATIONS_LIMIT = 10000000
GENERATION_SIZE = 50
AMOUNT_PARENTS_TO_KEEP = int(GENERATION_SIZE * 0.2)
BEST_GENE_GENERATION_LIMIT = 100

MAX_CHALLENGE_SIZE = 30
MIN_CHALLENGE_SIZE = 10

MAX_CITIES_DISTANCE = 10000
MIN_CITIES_DISTANCE = 10

WAIT_TIME_FOR_NEW_GENERATION = 0.15

CITIES = list({
    "São Paulo",
    "Rio de Janeiro",
    "Brasília",
    "Salvador",
    "Fortaleza",
    "Belo Horizonte",
    "Manaus",
    "Curitiba",
    "Recife",
    "Goiânia",
    "Belém",
    "Porto Alegre",
    "Guarulhos",
    "Campinas",
    "São Luís",
    "São Gonçalo",
    "Maceió",
    "Duque de Caxias",
    "Campo Grande",
    "Natal",
    "Teresina",
    "São Bernardo do Campo",
    "Nova Iguaçu",
    "João Pessoa",
    "São José dos Campos",
    "Santo André",
    "Ribeirão Preto",
    "Jaboatão dos Guararapes",
    "Osasco",
    "Uberlândia",
    "Sorocaba",
    "Contagem",
    "Aracaju",
    "Feira de Santana",
    "Cuiabá",
    "Joinville",
    "Aparecida de Goiânia",
    "Londrina",
    "Juiz de Fora",
    "Ananindeua",
    "Porto Velho",
    "Serra",
    "Niterói",
    "Belford Roxo",
    "Caxias do Sul",
    "Campos dos Goytacazes",
    "Macapá",
    "Florianópolis",
    "Vila Velha",
    "Mauá",
    "São João de Meriti",
    "São José do Rio Preto",
    "Mogi das Cruzes",
    "Betim",
    "Santos",
    "Diadema",
    "Maringá",
    "Jundiaí",
    "Campina Grande",
    "Montes Claros",
    "Rio Branco",
    "Piracicaba",
    "Carapicuíba",
    "Boa Vista",
    "Olinda",
    "Anápolis",
    "Cariacica",
    "Bauru",
    "Itaquaquecetuba",
    "São Vicente",
    "Vitória",
    "Caucaia",
    "Caruaru",
    "Blumenau",
    "Franca",
    "Ponta Grossa",
    "Petrolina",
    "Canoas",
    "Pelotas",
    "Vitória da Conquista",
    "Ribeirão das Neves",
    "Uberaba",
    "Paulista",
    "Cascavel",
    "Praia Grande",
    "São José dos Pinhais",
    "Guarujá",
    "Taubaté",
    "Petrópolis",
    "Limeira",
    "Santarém",
    "Camaçari",
    "Palmas",
    "Suzano",
    "Mossoró",
    "Taboão da Serra",
    "Várzea Grande",
    "Sumaré",
    "Santa Maria",
    "Gravataí",
    "Governador Valadares",
    "Marabá",
    "Juazeiro do Norte",
    "Barueri",
    "Embu das Artes",
    "Volta Redonda",
    "Ipatinga",
    "Parnamirim",
    "Imperatriz",
    "Foz do Iguaçu",
    "Macaé",
    "Viamão",
    "São Carlos",
    "Indaiatuba",
    "Cotia",
    "Novo Hamburgo",
    "São José",
    "Magé",
    "Colombo",
    "Itaboraí",
    "Sete Lagoas",
    "Americana",
    "Marília",
    "Divinópolis",
    "Itapevi",
    "São Leopoldo",
    "Araraquara",
    "Rio Verde",
    "Jacareí",
    "Rondonópolis",
    "Arapiraca",
    "Hortolândia",
    "Presidente Prudente",
    "Maracanaú",
    "Dourados",
    "Chapecó",
    "Cabo Frio",
    "Itajaí",
    "Santa Luzia",
    "Juazeiro",
    "Criciúma",
    "Itabuna",
    "Águas Lindas de Goiás",
    "Rio Grande",
    "Alvorada",
    "Cachoeiro de Itapemirim",
    "Sobral",
    "Luziânia",
    "Parauapebas",
    "Cabo de Santo Agostinho",
    "Rio Claro",
    "Angra dos Reis",
    "Passo Fundo",
    "Castanhal",
    "Lauro de Freitas",
    "Araçatuba",
    "Ferraz de Vasconcelos",
    "Santa Bárbara d'Oeste",
    "Nova Friburgo",
    "Barra Mansa",
    "Nossa Senhora do Socorro",
    "Teresópolis",
    "Guarapuava",
    "Araguaína",
    "Ibirité",
    "Jaraguá do Sul",
    "São José de Ribamar",
    "Mesquita",
    "Francisco Morato",
    "Itapecerica da Serra",
    "Itu",
    "Linhares",
    "Palhoça",
    "Timon",
    "Bragança Paulista",
    "Valparaíso de Goiás",
    "Pindamonhangaba",
    "Poços de Caldas",
    "Caxias",
    "Itapetininga",
    "Nilópolis",
    "Ilhéus",
    "Maricá",
    "São Caetano do Sul",
    "Teixeira de Freitas",
    "Camaragibe",
    "Abaetetuba",
    "Lages",
    "Jequié",
    "Barreiras",
    "Paranaguá",
    "Franco da Rocha",
    "Parnaíba",
    "Patos de Minas",
    "Mogi Guaçu",
    "Alagoinhas",
    "Pouso Alegre",
    "Rio das Ostras",
    "Queimados",
    "Jaú",
    "Porto Seguro",
    "Botucatu",
    "Araucária",
    "Sinop",
    "Atibaia",
    "Balneário Camboriú",
    "Sapucaia do Sul",
    "Toledo",
    "Teófilo Otoni",
    "Garanhuns",
    "Santana de Parnaíba",
    "Vitória de Santo Antão",
    "Cametá",
    "Barbacena",
    "Santa Rita",
    "Sabará",
    "Varginha",
    "Apucarana",
    "Brusque",
    "Simões Filho",
    "Araras",
    "Itaguaí",
    "Araruama",
    "Pinhais",
    "Crato",
    "Campo Largo",
    "Marituba",
    "Resende",
    "Cubatão",
    "São Mateus",
    "Santa Cruz do Sul",
    "Cachoeirinha",
    "Itapipoca",
    "Valinhos",
    "Maranguape",
    "Ji-Paraná",
    "Conselheiro Lafaiete",
    "São Félix do Xingu",
    "Bragança",
    "Vespasiano",
    "Trindade",
    "Uruguaiana",
    "Sertãozinho",
    "Jandira",
    "Guarapari",
    "Barcarena",
    "Birigui",
    "Ribeirão Pires",
    "Arapongas",
    "Codó",
    "Colatina",
    "Votorantim",
    "Paço do Lumiar",
    "Barretos",
    "Catanduva",
    "Várzea Paulista",
    "Guaratinguetá",
    "Tatuí",
    "Formosa",
    "Caraguatatuba",
    "Três Lagoas",
    "Santana",
    "Bagé",
    "Itatiba",
    "Bento Gonçalves",
    "Itabira",
    "Salto",
    "Almirante Tamandaré",
    "Paulo Afonso",
    "Poá",
    "Araguari",
    "Igarassu",
    "Novo Gama",
    "Ubá",
    "Senador Canedo",
    "Passos",
    "Altamira",
    "Parintins",
    "Tucuruí",
    "Ourinhos",
    "Eunápolis",
    "São Lourenço da Mata",
    "Paragominas",
    "Piraquara",
    "Açailândia",
    "Umuarama",
    "Corumbá",
    "Coronel Fabriciano",
    "Paulínia",
    "Catalão",
    "Muriaé",
    "Santa Cruz do Capibaribe",
    "Ariquemes",
    "Patos",
    "Cambé",
    "Tailândia",
    "Araxá",
    "Erechim",
    "Tubarão",
    "Bacabal",
    "Japeri",
    "Itumbiara",
    "Ituiutaba",
    "São Pedro da Aldeia",
    "Lagarto",
    "Assis",
    "Lavras",
    "Tangará da Serra",
    "Leme",
    "Itaperuna",
    "Breves",
    "Nova Serrana",
    "Iguatu",
    "São Gonçalo do Amarante",
    "Itanhaém",
    "Santo Antônio de Jesus",
    "Caieiras",
    "Itacoatiara",
    "Itaituba",
    "Aracruz",
    "Jataí",
    "Barra do Piraí",
    "Fazenda Rio Grande",
    "Mairiporã"
})
