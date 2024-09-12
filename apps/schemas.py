import graphene
from django.contrib.messages import success
from graphene_django import DjangoObjectType

from apps.models import Product, Category, User


# class ProductType(DjangoObjectType):
#     class Meta:
#         model = Product
#         fields = "__all__"
#

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = "__all__"
#
#
# class UpdateProduct(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         name = graphene.String(required=True)
#         price = graphene.Float(required=True)
#         discount = graphene.Float(required=True)
#         image = graphene.String()
#         description = graphene.String()
#         category = graphene.List(CategoryType)
#         owner = graphene.List(UserType)
#         updated_at=graphene.DateTime()
#         created_at=graphene.DateTime()
#
#
#     product = graphene.Field(ProductType)
#
#     def mutate(self, info, id, name, price, discount, image, description, category, owner, updated_at, created_at):
#         product = Product.objects.get(id=id)
#
#         if name:
#             product.name = name
#             product.price = price
#             product.discount = discount
#             product.image = image
#             product.description = description
#             product.category = category
#             product.owner = owner
#             product.updated_at = updated_at
#             product.created_at = created_at
#
#         product.save()
#         return UpdateProduct(product=product)
#
#
# class DeleteProduct(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#
#     success = graphene.Boolean()
#
#     def mutate(self, info, id):
#         try:
#             product = Product.objects.get(id=id)
#             product.delete()
#             return DeleteProduct(success=True, )
#         except Product.DoesNotExist:
#             return DeleteProduct(product=Product)
#
#
# class CreateProduct(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#
#     product = graphene.Field(ProductType)
#
#     def mutate(self, info, id, name, price, discount, image, description, category, owner, updated_at, created_at):
#         """
#         The mutate function is the function that will be called when a client
#         makes a request to this mutation. It takes in four arguments:
#         self, info, title and content. The first two are required by all mutations;
#         the last two are the arguments we defined in our CreatePostInput class.
#
#         :param self: Access the object's attributes and methods
#         :param info: Access the context of the request
#         :param title: Create a new post with the title provided
#         :param content: Pass the content of the post
#         :param author_id: Get the author object from the database
#         :return: A createpost object
#         """
#         product = Product.objects.create(
#         name=name,
#         price = price,
#         discount = discount,
#         image = image,
#         description = description,
#         category = category,
#         owner = owner,
#         updated_at = updated_at,
#         created_at = created_at
#         )
#         return CreateProduct(product=product)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        """
        The mutate function is the function that will be called when a client
        makes a request to this mutation. It takes in four arguments:
        self, info, title and content. The first two are required by all mutations;
        the last two are the arguments we defined in our CreatePostInput class.

        :param self: Access the object's attributes and methods
        :param info: Access the context of the request
        :param title: Create a new post with the title provided
        :param content: Pass the content of the post
        :param author_id: Get the author object from the database
        :return: A createpost object
        """
        category = Category.objects.create(
            name=name
        )
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, id):
        category = Category.objects.get(id=id)

        if name:
            category.name = name

        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.String()

    # def mutate(self, info, id):
    #     try:
    #         category = Category.objects.get(id=id)
    #         category.delete()
    #         return DeleteCategory(success=True,)
    #     except Product.DoesNotExist:
    #         return DeleteCategory(category=Category)

    def mutate(self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        if category.delete:
            return DeleteCategory(success="muvaffaqiyatli o'chirildi!")
        elif Product.DoesNotExist:
            return DeleteCategory(category=Category)
        else:
            return DeleteCategory(success="ochmadi")


class Query(graphene.ObjectType):
    # products = graphene.List(ProductType)
    categories = graphene.List(CategoryType, description='Bu kategoriya hisoblanadi')

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
