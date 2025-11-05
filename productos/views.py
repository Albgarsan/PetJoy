from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Producto, Categoria, Marca


def catalogo_productos(request):
    """Vista del catálogo de productos con filtros"""
    productos = Producto.objects.filter(esta_disponible=True)
    
    # Filtro por categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    # Filtro por marca
    marca_id = request.GET.get('marca')
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    
    # Filtro por género
    genero = request.GET.get('genero')
    if genero:
        productos = productos.filter(genero=genero)
    
    # Búsqueda
    query = request.GET.get('q')
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categoria__nombre__icontains=query) |
            Q(marca__nombre__icontains=query)
        )
    
    # Paginación
    paginator = Paginator(productos, 12)
    page = request.GET.get('page')
    productos_paginados = paginator.get_page(page)
    
    context = {
        'productos': productos_paginados,
        'categorias': Categoria.objects.all(),
        'marcas': Marca.objects.all(),
        'query': query,
    }
    return render(request, 'productos/catalogo.html', context)


def detalle_producto(request, slug):
    """Vista de detalle de un producto"""
    producto = get_object_or_404(Producto, slug=slug, esta_disponible=True)
    
    # Productos relacionados (misma categoría)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        esta_disponible=True
    ).exclude(id=producto.id)[:4]
    
    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
    }
    return render(request, 'productos/detalle.html', context)


def productos_por_categoria(request, categoria_id):
    """Vista de productos por categoría"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria, esta_disponible=True)
    
    # Paginación
    paginator = Paginator(productos, 12)
    page = request.GET.get('page')
    productos_paginados = paginator.get_page(page)
    
    context = {
        'categoria': categoria,
        'productos': productos_paginados,
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'productos/por_categoria.html', context)
