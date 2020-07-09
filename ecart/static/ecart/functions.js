

 console.log('working');
      if(localStorage.getItem('cart')==null){
      var cart={};
      document.getElementById('clearcart').style.visibility="hidden";
      }
      else{
        cart=JSON.parse(localStorage.getItem('cart'));
        updatecart(cart);
        document.getElementById('clearcart').style.visibility="visible";
      }

      //$('.cart').click(function (){
function cartclick(event){
      var strid=event.id;
      console.log(strid);
      if(cart[strid]!=undefined){
        qty=cart[strid][0]+1;
        name=document.getElementById('name'+strid).innerHTML;
        price=document.getElementById('price'+strid).innerHTML;
        //console.log("Price "+price);
        cart[strid]=[qty,name,price.slice(9,)]
        updatecart(cart);
      }
      else{
        qty=1;
        name=document.getElementById('name'+strid).innerHTML
        price=document.getElementById('price'+strid).innerHTML;
        console.log("Price"+price.slice(9,))
        console.log("Price"+price)
        cart[strid]=[qty,name,price.slice(9,)]
        document.getElementById('clearcart').style.visibility="visible";
        updatecart(cart)

      }


 // This below code is to get count of values in dictionary.
  /*  var car=new Array();
    car=Object.values(cart);
        var text=0;
        for (i = 0; i < car.length; i++) {
            text += car[i] ;
            console.log(cart[i])
        }
        console.log(text); */
      };

     $('#popcart').popover();
     updatepopover(cart);

     function updatepopover(cart){
        var con=""
        con="<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
        i=1;
        for ( var item in cart) {
                  con=con+i+"."+document.getElementById('name'+item).innerHTML+"<b> QTY:"+cart[item][0]+"</b><br>"
                  i+=1;

          }

          con+="</div><a href='/shop/checkout'><button class='btn btn-primary' id ='checkout'>Checkout</button></a>"

          document.getElementById("popcart").setAttribute('data-content', con);

        $('#popcart').popover('show');
        };

    function updatecart(cart){
            for (var item in cart){
                    console.log("itemmmm"+item)
                  document.getElementById('div'+item).innerHTML="<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
            }
        localStorage.setItem('cart', JSON.stringify(cart));

        document.getElementById('cart').innerHTML = Object.keys(cart).length;
        updatepopover(cart);

    }
    $('.divpr').on("click","button.minus",function(){
        a=this.id.slice(7,);
        console.log(cart['pr'+a][0]);
        cart['pr'+a][0]=cart['pr'+a][0]-1;
        cart['pr'+a][0]=Math.max(0,cart['pr'+a][0]);
        document.getElementById('valpr'+a).innerHTML=cart['pr'+a][0];
        if (cart['pr'+a][0]==0){
            console.log("ZERO");
            console.log(cart);
            delete cart['pr'+a];
            console.log(cart)
            document.getElementById('divpr'+a).innerHTML="<button class='btn btn-primary cart' id='pr"+a+"' onclick='cartclick(this)'>Add To Cart</button>";
        };
        updatecart(cart);
    });

    $('.divpr').on("click","button.plus",function(){
        a=this.id.slice(6,);
        cart['pr'+a][0]=cart['pr'+a][0]+1;
        document.getElementById('valpr'+a).innerHTML=cart['pr'+a][0];
        updatecart(cart);
    });

    $('#clearcart').click(function(){
    localStorage.removeItem("cart");
    });


