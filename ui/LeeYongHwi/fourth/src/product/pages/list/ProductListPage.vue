<template lang="">
    <v-container>
        <h2>Product List</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name: 'ProductRegisterPage' }">
                상품 등록
            </router-link>
        </div>
        <v-data-table
            v-model:items-per-page="perPage"
            :headers="headerTitle"
            :items="pagedItems"
            v-model:pagination="pagination"
            class="elevation-1"
            @click:row="readRow"
            item-value="productId"/>
        <v-pagination
            v-model="pagination.page"
            :length="Math.ceil(products.length / perPage)"
            color="primary"
            @input="updateItems"/>
    </v-container>
</template>

<script>

import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
    components: {

    },
    computed: {
        ...mapState(productModule, ['products']),
        pagedItems () {
            const startIdx = (this.pagination.page - 1) * this.perPage
            const endIdx = startIdx + this.perPage
            return this.products.slice(startIdx, endIdx)
        }
    },
    mounted () {
        this.requestProductListToDjango()
    },
    methods: {
        ...mapActions(productModule, ['requestProductListToDjango']),
        readRow (event, { item }) {
            this.$router.push({
                name: 'ProductReadPage',
                params: { productId: item['productId'].toString() }
            })
        }
            },
    data () {
        return {
            headerTitle: [
                {
                    title: 'No',
                    align: 'start',
                    sortable: true,
                    key: 'productId',
                },
                { title: '상품명', align: 'end', key: 'productName' },
                { title: '가격', align: 'end', key: 'price' },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>