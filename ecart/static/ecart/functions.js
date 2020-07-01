

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

      $('.cart').click(function (){

      var strid=this.id.toString();
      if(cart[strid]!=undefined){
        cart[strid]=cart[strid]+1;
        updatecart(cart);
      }
      else{
        cart[strid]=1;
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

      });


     $('#popcart').popover();
     updatepopover(cart);

     function updatepopover(cart){
        var con=""
        con="<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
        i=1;
        for ( var item in cart) {
          //console.log("popover")
          //console.log(i)
          con=con+i+"."+document.getElementById('name'+item).innerHTML+"<b> QTY:"+cart[item]+"</b><br>"

          i+=1;

          }




          con+="</div><a href='/shop/checkout'><button class='btn btn-primary' id ='checkout'>Checkout</button></a>"
          //<button class='btn btn-primary' type='button'>Click Me!</button>";
            //<span><a href='/shop/checkout/'>HI</a> </span>
          //console.log(con);

          document.getElementById("popcart").setAttribute('data-content', con);

        $('#popcart').popover('show');
        };

    function updatecart(cart){
        console.log(cart);
        for (var item in cart){
        console.log(cart[item]);
//-below code is for removing 0 elements from cart. But its not working.
        /*  if (cart[item]==0){
            console.log("Item is 0 :"+item);
            delete cart.item;
            console.log(cart);
            continue;
          } */

        console.log(item);
            document.getElementById('div'+item).innerHTML="<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
            }
            //console.log("CART AFTER DELETE "+JSON.stringify(cart))
        localStorage.setItem('cart', JSON.stringify(cart));
        document.getElementById('cart').innerHTML = Object.keys(cart).length;
        updatepopover(cart);

    }
    $('.divpr').on("click","button.minus",function(){
        console.log("minus")
        a=this.id.slice(7,);
        console.log(a);
        cart['pr'+a]=cart['pr'+a]-1;
        cart['pr'+a]=Math.max(0,cart['pr'+a]);
        document.getElementById('valpr'+a).innerHTML=cart['pr'+a];
        updatecart(cart);


    })
    $('.divpr').on("click","button.plus",function(){
        console.log("plus")
        a=this.id.slice(6,);
        cart['pr'+a]=cart['pr'+a]+1;
        document.getElementById('valpr'+a).innerHTML=cart['pr'+a];
        updatecart(cart);

    })

    $('#clearcart').click(function(){
    localStorage.removeItem("cart");

    });


