package interfaceJava;

import java.awt.Button;
import java.awt.Label;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.JLabel;

public class FuncoeExtras {
	
	JLabel lblimagem;
	JLabel lblhistograma;
	Label nomeImagem;
	Label textOutput;
	
	String arq;
	ImageIcon histo;
	ImageIcon imagem;
	String[] cmdExecEntrada;
	String[] cmdExecFiltro;
	JFileChooser jfc;
	public String camImagem;
	public String camImagemEditada;
	
	public void definirDiretorios(int i) {
		
		if( i == 0 ) {//pessoal
			//Funcao substituirTexto
			arq = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\main.py",
	      		      "--img",
	      		      ""
    		    };
			cmdExecEntrada = entrada;
			
			String[] filtro = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\filtro.py",
	      		      "--img",
	      		      ""
  		    };
			cmdExecFiltro = filtro;
			
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens");	//pc pessoal
			
		}else { //projeto
			//Funcao substituirTexto
			arq = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
      		      "python",
      		      "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py",
      		      "--img",
      		      ""
      		    };
			cmdExecEntrada = entrada;
			
			String[] filtro = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\filtro.py",
	      		      "--img",
	      		      ""
		    };
			cmdExecFiltro = filtro;
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\imagens");	//pc Projeto
		}

	}
	
	public void ExecutarScriptPython(String saida) {
        try {
        	cmdExecEntrada[3] = saida; 
		    Runtime.getRuntime().exec(cmdExecEntrada);
		    
		    Thread.sleep(2200);

        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	public void ExeScriptPythonFiltro(String saida) {
        try {
        	cmdExecFiltro[3] = saida; 
		    Runtime.getRuntime().exec(cmdExecFiltro);
		    
		    Thread.sleep(2200);

        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	
}
