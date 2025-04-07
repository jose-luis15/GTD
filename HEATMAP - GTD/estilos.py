html = '''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                text-decoration: none;
                font-family: 'Open Sans', sans-serif;
            }

            .header-content {
                max-width: 1450px; /*Esto da espacios tanto a la derecha como a la izquierad de nuestra pagina*/
                margin: auto;
                display: flex;
                justify-content: space-between;
                background-color: #F7A403;
                height: 60PX;
                max-width: 1200px
            }

            .logo {
                    height: 60px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .logo h1 b {
                    color: #ffffff;
                }

                .menu {
                    height: 60px;
                }

                .menu nav {
                    height: 100%;
                }

                .menu nav ul {
                    height: 100%;
                    display: flex;
                    list-style: none;
                    position: relative;
                }

                .menu nav ul li {
                    height: 100%;
                    margin: 0 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    position: relative;
                }

                .social-list a{
                    padding: 0 15px;
                    font-size: 35px;
                    color: #375D9F;
                }

                .social-list a:hover{
                    color: white;
                    transition: color 0.3s;
                }
        </style>

        <script src="https://kit.fontawesome.com/5eb7f44b07.js" crossorigin="anonymous"></script>

        <div class="header" style="background-color: #F7A403;">
            <div class="header-content">
                    <div class="logo">
                        <a href="https://www.gtdperu.com/"><img
                                src="https://www.gtdperu.com/image/layout_set_logo?img_id=3971675&t=1679053451501" style="height:50px; padding: 5px;"></a>
                        <h1>GTD<b>Perú</b></h1>
                    </div>
            
                    <div class="menu">
                        <nav class="social">
                            <ul class="social-list">
                                <li><a href="mailto:gtdperu_factibilidades.pext@grupogtd.com" class="fa-solid fa-envelope"></a></li>
                                <li><a href="https://www.linkedin.com/company/gtdperu/mycompany/" class="fa-brands fa-linkedin"></a></li>
                            </ul>
                        </nav>
                    </div>
            </div>
        </div>
'''
